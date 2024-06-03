
# Blood test report analysis

## Overview

This project sets up a series of agents and tasks using the `crew.ai` framework to analyze a blood report and provide health recommendations based on the analysis and related internet articles. The project uses tools for reading directories, files, and PDFs, as well as searching the web for relevant health articles.

## Setup

### Prerequisites

- Python 3.6 or higher
- Required Python packages: `crewai`, `crewai_tools`, `fitz` (PyMuPDF) , `openai`

### Installation

1. **Clone the repository:**

    \`\`\`bash
    git clone https://github.com/yourusername/wingify_final_submission.git
    cd wingify_final_submission
    \`\`\`

2. **Install the required Python packages:**

    \`\`\`bash
    pip install crewai crewai_tools pymupdf
    \`\`\`

3. **Set up your API keys:**

    Replace the placeholders in the script with your actual API keys for Serper and OpenAI.

    \`\`\`python
    os.environ["SERPER_API_KEY"] = "your-serper-api-key"
    os.environ["OPENAI_API_KEY"] = "your-openai-api-key"
    os.environ["OPENAI_MODEL_NAME"] = "gpt-3.5-turbo"
    \`\`\`

## Usage

### Directory Structure

- Place the blood report PDF in the directory specified by `docs_tool`.
- Ensure the directory path in `docs_tool` and `output_file` for the health blogger task are correct.

### Script Execution

1. **Convert PDF to Text:**

    The script includes a function `pdf_to_text` to convert the PDF report to a text file for easy readability.

    \`\`\`python
    pdf_path = r'C:\\Users\\SURFACE\\Desktop\\wingify_final_submission\\your_blood_report.pdf'
    txt_path = 'output.txt'
    pdf_to_text(pdf_path, txt_path)
    \`\`\`

2. **Run the script:**

    The main script sets up the agents and tasks, then kicks off the process with the provided inputs.

    \`\`\`python
    inputs = {
        'topic': 'Blood Reports and Health',
        'text_file' : txt_path
    }

    crew.kickoff(inputs=inputs)
    \`\`\`

## Agents and Tasks

### Agents

1. **Blood Report Analyst**
    - **Role:** Analyze the blood test report and summarize key points.
    - **Goal:** Provide actionable insights based on health indicators in the blood report.
    - **Tools:** DirectoryReadTool, FileReadTool, PDFSearchTool.
    - **Verbose:** True.

2. **Health Advisor**
    - **Role:** Provide health recommendations based on the blood report analysis and internet articles.
    - **Goal:** Offer practical health advice and cite sources.
    - **Tools:** SerperDevTool, WebsiteSearchTool, DirectoryReadTool, FileReadTool.
    - **Verbose:** True.

### Tasks

1. **Analyze Blood Report**
    - **Description:** Analyze the blood test report and summarize key findings.
    - **Expected Output:** JSON file with summarized report.
    - **Agent:** Blood Report Analyst.

2. **Generate Health Feedback and URLs**
    - **Description:** Provide health recommendations based on blood report analysis and related articles.
    - **Expected Output:** JSON file with health recommendations and URLs.
    - **Agent:** Health Advisor.
    - **Context:** Analysis from the blood report task.
    - **Output Directory:** `C:\\Users\\SURFACE\\Desktop\\wingify_final_submission`.

## Notes

- Ensure that the specified paths for tools and output directories are correctly set.
- The `kickoff` method initiates the task sequence with the given inputs.
- Modify API keys and paths as necessary for your environment.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- Thanks to the creators of `crewai` and `crewai_tools` for the powerful framework.
- Special thanks to [Wingify] for inspiring this project.
"""

