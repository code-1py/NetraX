from .base import NetraxError


class AIProviderError(NetraxError):
    """An AI provider request failed.

    Attributes:
        provider: Name of the provider associated with the failed request.
        status_code: HTTP status code returned by the provider.
        response_text: Response body returned by the provider.
    """

    def __init__(self, provider: str, status_code: int, response_text: str):
        self.provider = provider
        self.status_code = status_code
        self.response_text = response_text
        super().__init__(
            f"AI provider request failed for {provider} with status code {status_code}.\nResponse text: {response_text}"
        )


class ReportGenerationError(NetraxError):
    """An AI report could not be generated.

    Attributes:
        provider: Name of the provider used for the request.
        stderr: Error text associated with report generation.
    """

    def __init__(self, provider: str, stderr: str):
        self.provider = provider
        self.stderr = stderr
        super().__init__(
            f"Failed to generate AI report using {provider}.\nstderr: {stderr if stderr else 'No error output'}"
        )
