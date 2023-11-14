#  Copyright (c) ZenML GmbH 2023. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""ModelVersion user facing interface to pass into pipeline or step."""

from typing import (
    TYPE_CHECKING,
    Any,
    Dict,
    List,
    Optional,
    Union,
)
from uuid import UUID

from pydantic import BaseModel, PrivateAttr, root_validator

from zenml.enums import ModelStages
from zenml.exceptions import EntityExistsError, ReservedNameError
from zenml.logger import get_logger

if TYPE_CHECKING:
    from zenml.models import (
        ArtifactResponseModel,
        ModelResponseModel,
        ModelVersionResponseModel,
        PipelineRunResponseModel,
    )

logger = get_logger(__name__)


class ModelVersion(BaseModel):
    """ModelVersion class to pass into pipeline or step to set it into a model context.

    name: The name of the model.
    license: The license under which the model is created.
    description: The description of the model.
    audience: The target audience of the model.
    use_cases: The use cases of the model.
    limitations: The known limitations of the model.
    trade_offs: The tradeoffs of the model.
    ethics: The ethical implications of the model.
    tags: Tags associated with the model.
    version: The model version name, number or stage is optional and points model context
        to a specific version/stage. If skipped new model version will be created.
    save_models_to_registry: Whether to save all ModelArtifacts to Model Registry,
        if available in active stack.
    """

    name: str
    license: Optional[str]
    description: Optional[str]
    audience: Optional[str]
    use_cases: Optional[str]
    limitations: Optional[str]
    trade_offs: Optional[str]
    ethics: Optional[str]
    tags: Optional[List[str]]
    version: Optional[Union[ModelStages, int, str]]
    save_models_to_registry: bool = True

    suppress_class_validation_warnings: bool = False
    was_created_in_this_run: bool = False

    _model_id: UUID = PrivateAttr(None)
    _id: UUID = PrivateAttr(None)
    _number: int = PrivateAttr(None)

    #########################
    #    Public methods     #
    #########################
    @property
    def all_model_versions(self) -> List["ModelVersion"]:
        """Get all model versions for current model from the Model Control Plane.

        Returns:
            A list of ModelVersion objects registered within current model.
        """
        return self._get_or_create_model().versions

    @property
    def id(self) -> UUID:
        """Get version id from  the Model Control Plane.

        Returns:
            ID of the model version or None, if model version
                doesn't exist and can only be read given current
                config (you used stage name or number as
                a version name).
        """
        if self._id is None:
            try:
                self._get_or_create_model_version()
            except ReservedNameError:
                logger.info(
                    f"Model version `{self.version}` doesn't exist "
                    "and cannot be fetched from the Model Control Plane."
                )
        return self._id

    @property
    def model_id(self) -> UUID:
        """Get model id from  the Model Control Plane.

        Returns:
            The UUID of the model containing this model version.
        """
        if self._model_id is None:
            self._get_or_create_model()
        return self._model_id

    @property
    def number(self) -> int:
        """Get version number from  the Model Control Plane.

        Returns:
            Number of the model version or None, if model version
                doesn't exist and can only be read given current
                config (you used stage name or number as
                a version name).
        """
        if self._number is None:
            try:
                self._get_or_create_model_version()
            except ReservedNameError:
                logger.info(
                    f"Model version `{self.version}` doesn't exist "
                    "and cannot be fetched from the Model Control Plane."
                )
        return self._number

    @property
    def stage(self) -> Optional[ModelStages]:
        """Get version stage from  the Model Control Plane.

        Returns:
            Stage of the model version or None, if model version
                doesn't exist and can only be read given current
                config (you used stage name or number as
                a version name).
        """
        try:
            stage = self._get_or_create_model_version().stage
            if stage:
                return ModelStages(stage)
        except ReservedNameError:
            logger.info(
                f"Model version `{self.version}` doesn't exist "
                "and cannot be fetched from the Model Control Plane."
            )
        return None

    def get_model_artifact(
        self,
        name: str,
        version: Optional[str] = None,
        pipeline_name: Optional[str] = None,
        step_name: Optional[str] = None,
    ) -> Optional["ArtifactResponseModel"]:
        """Get the model artifact linked to this model version.

        Args:
            name: The name of the model artifact to retrieve.
            version: The version of the model artifact to retrieve (None for latest/non-versioned)
            pipeline_name: The name of the pipeline-generated the model artifact.
            step_name: The name of the step-generated the model artifact.

        Returns:
            Specific version of the model artifact or None
        """
        return self._get_or_create_model_version().get_model_artifact(
            name=name,
            version=version,
            pipeline_name=pipeline_name,
            step_name=step_name,
        )

    def get_data_artifact(
        self,
        name: str,
        version: Optional[str] = None,
        pipeline_name: Optional[str] = None,
        step_name: Optional[str] = None,
    ) -> Optional["ArtifactResponseModel"]:
        """Get the data artifact linked to this model version.

        Args:
            name: The name of the data artifact to retrieve.
            version: The version of the data artifact to retrieve (None for latest/non-versioned)
            pipeline_name: The name of the pipeline generated the data artifact.
            step_name: The name of the step generated the data artifact.

        Returns:
            Specific version of the data artifact or None
        """
        return self._get_or_create_model_version().get_data_artifact(
            name=name,
            version=version,
            pipeline_name=pipeline_name,
            step_name=step_name,
        )

    def get_endpoint_artifact(
        self,
        name: str,
        version: Optional[str] = None,
        pipeline_name: Optional[str] = None,
        step_name: Optional[str] = None,
    ) -> Optional["ArtifactResponseModel"]:
        """Get the endpoint artifact linked to this model version.

        Args:
            name: The name of the endpoint artifact to retrieve.
            version: The version of the endpoint artifact to retrieve (None for latest/non-versioned)
            pipeline_name: The name of the pipeline generated the endpoint artifact.
            step_name: The name of the step generated the endpoint artifact.

        Returns:
            Specific version of the endpoint artifact or None
        """
        return self._get_or_create_model_version().get_endpoint_artifact(
            name=name,
            version=version,
            pipeline_name=pipeline_name,
            step_name=step_name,
        )

    def get_pipeline_run(self, name: str) -> "PipelineRunResponseModel":
        """Get pipeline run linked to this version.

        Args:
            name: The name of the pipeline run to retrieve.

        Returns:
            PipelineRun as PipelineRunResponseModel
        """
        return self._get_or_create_model_version().get_pipeline_run(name=name)

    def set_stage(
        self, stage: Union[str, ModelStages], force: bool = False
    ) -> "ModelVersion":
        """Sets this Model Version to a desired stage.

        Args:
            stage: the target stage for model version.
            force: whether to force archiving of current model version in target stage or raise.

        Returns:
            Updated Model Version object.
        """
        return self._get_or_create_model_version().set_stage(
            stage=stage, force=force
        )

    #########################
    #   Internal methods    #
    #########################

    class Config:
        """Config class."""

        smart_union = True

    def __eq__(self, other: object) -> bool:
        """Check two ModelVersions for equality.

        Args:
            other: object to compare with

        Returns:
            True, if equal, False otherwise.
        """
        if not isinstance(other, ModelVersion):
            return NotImplemented
        if self.name != other.name:
            return False
        if self.name == other.name and self.version == other.version:
            return True
        self_mv = self._get_or_create_model_version()
        other_mv = other._get_or_create_model_version()
        return self_mv.id == other_mv.id

    @root_validator(pre=True)
    def _root_validator(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Validate all in one.

        Args:
            values: Dict of values.

        Returns:
            Dict of validated values.
        """
        suppress_class_validation_warnings = values.get(
            "suppress_class_validation_warnings", False
        )
        version = values.get("version", None)

        if (
            version in [stage.value for stage in ModelStages]
            and not suppress_class_validation_warnings
        ):
            logger.info(
                f"`version` `{version}` matches one of the possible `ModelStages` and will be fetched using stage."
            )
        if str(version).isnumeric() and not suppress_class_validation_warnings:
            logger.info(
                f"`version` `{version}` is numeric and will be fetched using version number."
            )
        values["suppress_class_validation_warnings"] = True
        return values

    def _validate_config_in_runtime(self) -> None:
        """Validate that config doesn't conflict with runtime environment."""
        self._get_or_create_model_version()

    def _get_or_create_model(self) -> "ModelResponseModel":
        """This method should get or create a model from Model Control Plane.

        New model is created implicitly, if missing, otherwise fetched.

        Returns:
            The model based on configuration.
        """
        from zenml.client import Client
        from zenml.models.model_models import ModelRequestModel

        zenml_client = Client()
        try:
            model = zenml_client.zen_store.get_model(
                model_name_or_id=self.name
            )
        except KeyError:
            model_request = ModelRequestModel(
                name=self.name,
                license=self.license,
                description=self.description,
                audience=self.audience,
                use_cases=self.use_cases,
                limitations=self.limitations,
                trade_offs=self.trade_offs,
                ethics=self.ethics,
                tags=self.tags,
                user=zenml_client.active_user.id,
                workspace=zenml_client.active_workspace.id,
            )
            model_request = ModelRequestModel.parse_obj(model_request)
            try:
                model = zenml_client.zen_store.create_model(
                    model=model_request
                )
                logger.info(f"New model `{self.name}` was created implicitly.")
            except EntityExistsError:
                # this is backup logic, if model was created somehow in between get and create calls
                pass
            finally:
                model = zenml_client.zen_store.get_model(
                    model_name_or_id=self.name
                )
        self._model_id = model.id
        return model

    def _get_model_version(self) -> "ModelVersionResponseModel":
        """This method gets a model version from Model Control Plane.

        Returns:
            The model version based on configuration.
        """
        from zenml.client import Client

        zenml_client = Client()
        return zenml_client.zen_store.get_model_version(
            model_name_or_id=self.name,
            model_version_name_or_number_or_id=self.version,
        )

    def _get_or_create_model_version(self) -> "ModelVersionResponseModel":
        """This method should get or create a model and a model version from Model Control Plane.

        A new model is created implicitly if missing, otherwise existing model is fetched. Model
        name is controlled by the `name` parameter.

        Model Version returned by this method is resolved based on model version:
        - If `version` is None, a new model version is created, if not created by other steps in same run.
        - If `version` is not None a model version will be fetched based on the version:
            - If `version` is set to an integer or digit string, the model version with the matching number will be fetched.
            - If `version` is set to a string, the model version with the matching version will be fetched.
            - If `version` is set to a `ModelStage`, the model version with the matching stage will be fetched.

        Returns:
            The model version based on configuration.

        Raises:
            ReservedNameError: if the model version needs to be created, but provided name is reserved
        """
        from zenml.client import Client
        from zenml.models.model_models import ModelVersionRequestModel

        model = self._get_or_create_model()

        zenml_client = Client()
        model_version_request = ModelVersionRequestModel(
            user=zenml_client.active_user.id,
            workspace=zenml_client.active_workspace.id,
            name=self.version,
            description=self.description,
            model=model.id,
        )
        mv_request = ModelVersionRequestModel.parse_obj(model_version_request)
        try:
            if not self.version:
                try:
                    from zenml import get_step_context

                    context = get_step_context()
                except RuntimeError:
                    pass
                else:
                    pipeline_mv = context.pipeline_run.config.model_version
                    if (
                        pipeline_mv
                        and pipeline_mv.was_created_in_this_run
                        and pipeline_mv.name == self.name
                    ):
                        self.version = pipeline_mv.version
                    else:
                        for step in context.pipeline_run.steps.values():
                            step_mv = step.config.model_version
                            if (
                                step_mv
                                and step_mv.was_created_in_this_run
                                and step_mv.name == self.name
                            ):
                                self.version = step_mv.version
                                break
            if self.version:
                model_version = self._get_model_version()
            else:
                raise KeyError
        except KeyError:
            if (
                self.version
                and str(self.version).lower() in ModelStages.values()
            ):
                raise ReservedNameError(
                    f"Cannot create a model version named {str(self.version)} as "
                    "it matches one of the possible model version stages. If you "
                    "are aiming to fetch model version by stage, check if the "
                    "model version in given stage exists. It might be missing, if "
                    "the pipeline promoting model version to this stage failed,"
                    " as an example. You can explore model versions using "
                    f"`zenml model version list {self.name}` CLI command."
                )
            if str(self.version).isnumeric():
                raise ReservedNameError(
                    f"Cannot create a model version named {str(self.version)} as "
                    "numeric model version names are reserved. If you "
                    "are aiming to fetch model version by number, check if the "
                    "model version with given number exists. It might be missing, if "
                    "the pipeline creating model version failed,"
                    " as an example. You can explore model versions using "
                    f"`zenml model version list {self.name}` CLI command."
                )
            model_version = zenml_client.zen_store.create_model_version(
                model_version=mv_request
            )
            self.version = model_version.name
            self.was_created_in_this_run = True
            logger.info(f"New model version `{self.version}` was created.")
        self._id = model_version.id
        self._model_id = model_version.model.id
        self._number = model_version.number
        return model_version

    def _merge(self, model_version: "ModelVersion") -> None:
        self.license = self.license or model_version.license
        self.description = self.description or model_version.description
        self.audience = self.audience or model_version.audience
        self.use_cases = self.use_cases or model_version.use_cases
        self.limitations = self.limitations or model_version.limitations
        self.trade_offs = self.trade_offs or model_version.trade_offs
        self.ethics = self.ethics or model_version.ethics
        if model_version.tags is not None:
            self.tags = list(
                {t for t in self.tags or []}.union(set(model_version.tags))
            )

    def __hash__(self) -> int:
        """Get hash of the `ModelVersion`.

        Returns:
            Hash function results
        """
        return hash(
            "::".join(
                (
                    str(v)
                    for v in (
                        self.name,
                        self.version,
                    )
                )
            )
        )