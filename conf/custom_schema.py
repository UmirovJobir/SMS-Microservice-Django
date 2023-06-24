from drf_spectacular.openapi import AutoSchema

from drf_spectacular.utils import OpenApiParameter


class CustomAutoSchema(AutoSchema):
    global_params = [
        OpenApiParameter(
            name="Language",
            type=str,
            location=OpenApiParameter.HEADER,
            description="`uz_cyrl` or `uz_latn` or `ru`",
        )
    ]

    def get_override_parameters(self):
        params = super().get_override_parameters()
        return params + self.global_params