
# Agentic AI: A Versatile Multi-Agent System

This project showcases an advanced Agentic AI application using Groq Llama 3.3 70B model. It employs multiple specialized agents to handle web searches, financial data analysis, and YouTube video comprehension. The application features an intuitive web-based playground interface for seamless interaction.

---

## Features

### 1. **Web Agent**
- **Role**: Searches the web for information using DuckDuckGo.
- **Capabilities**:
  - Performs general web searches.
  - Provides results with sources.
  - Summarizes news and updates.
- **Tools**: DuckDuckGo search integration.

### 2. **Finance Agent**
- **Role**: Gathers and analyzes financial data.
- **Capabilities**:
  - Retrieves stock prices, analyst recommendations, company information, and news.
  - Presents results in tables.
  - Assists users in making informed investment decisions.
- **Tools**: YFinanceTools with financial data features.

### 3. **YouTube Agent**
- **Role**: Analyzes and summarizes YouTube videos.
- **Capabilities**:
  - Extracts video metadata and captions.
  - Answers user questions based on video content.
  - Summarizes videos when provided with a URL.
- **Tools**: YouTubeTools for video analysis.

---

## Installation

### Prerequisites
1. **Python**: Ensure Python 3.8+ is installed.
2. **Dependencies**: Install required packages using `pip`.

### Setup
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and configure environment variables if needed:
   ```bash
   touch .env
   ```
   Example:
   ```env
   API_KEY=<your_api_key>
   DB_PATH=tmp/groq_agents.db
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. Open the web application in your browser:
   ```
   http://127.0.0.1:8000
   ```

---

## Usage

### Web Agent
- Ask questions requiring web searches.
- Provides sourced information using DuckDuckGo.

### Finance Agent
- Query for stock prices, recommendations, or news.
- Displays results in structured tables.

### YouTube Agent
- Provide a YouTube video URL.
- Summarizes videos or answers questions based on their content.

---

## File Structure
- `main.py`: Entry point of the application.
- `agents.py`: Defines agents with roles, tools, and instructions.
- `playground.py`: Configures the Playground interface.
- `requirements.txt`: Lists dependencies.
- `tmp/`: Stores SQLite databases for agent history and storage.

---

## Technologies Used
- **Model**: Groq Llama 3.3 70B (Versatile)
- **Tools**:
  - DuckDuckGo for web searches.
  - YFinance for financial data.
  - YouTubeTools for video analysis.
- **Backend**: SQLite for agent storage.
- **Frontend**: Playground interface for user interaction.

---

## Contributions
Feel free to contribute to the project by submitting issues or pull requests. Ensure proper documentation of new features or bug fixes.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Acknowledgments
Special thanks to the Groq and PHI teams for their advanced models and tools, making this project possible.

---

## Future Enhancements
- Integrate more agents for specialized domains (e.g., healthcare, education).
- Add real-time streaming capabilities for responses.
- Improve the user interface for a seamless experience.

---
