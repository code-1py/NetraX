from .base import NetraxError

class AIProviderError(NetraxError):
    """AI provider request failed."""
    def __init__(self, provider: str, status_code: int, response_text: str):
        self.provider = provider
        self.status_code = status_code
        self.response_text = response_text
        super().__init__(f"AI provider request failed for {provider} with status code {status_code}.\nResponse text: {response_text}")

class ReportGenerationError(NetraxError):
    """Failed to generate AI report."""
    def __init__(self, provider: str, stderr: str):
        self.provider = provider
        self.stderr = stderr
        super().__init__(f"Failed to generate AI report using {provider}.\nstderr: {stderr if stderr else 'No error output'}")