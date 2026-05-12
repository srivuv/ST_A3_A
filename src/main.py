from services.workflow_service import WorkflowService
from config import MODEL_OUTPUT_DIR
from app import MacroApp

def main() -> None:
    """Start the GUI-driven version of the project.
    """

    workflow = WorkflowService()
    workflow.run_full_pipeline()
    app = MacroApp(workflow.preprocessor, MODEL_OUTPUT_DIR/"macro_classifier.joblib")
    app.mainloop()

if __name__ == "__main__":
    main()
