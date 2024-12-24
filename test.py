from textwrap import dedent
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckdb import DuckDbTools
from dotenv import load_dotenv
load_dotenv()
duckdb_tools = DuckDbTools(create_tables=False, export_tables=False, summarize_tables=False)
duckdb_tools.create_table_from_path(
    path="https://drive.google.com/file/d/15VwhNGVcA8sZXRnij4C9UuTGniTwHlNI/view?usp=sharing",table="movies"
    )


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[duckdb_tools],
    markdown=True,
    show_tool_calls=True,
    additional_context=dedent("""\
    You have access to the following tables:
    - movies: Contains information about movies from IMDB.
    """),
)
agent.print_response("What is the highest rating of movies?", stream=False)