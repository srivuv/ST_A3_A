from src.services.workflow_service import WorkflowService
from src.config import MODEL_OUTPUT_DIR
from src.app import MacroApp

def main() -> None:
    """Start the GUI-driven version of the project.
    """

    workflow = WorkflowService()
    app = MacroApp(workflow.preprocessor, MODEL_OUTPUT_DIR/"macro_classifier.joblib")
    app.mainloop()

if __name__ == "__main__":
    main()
