from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, write_task
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Forming the tech-focused crew with some enhanced configurations
try:
    crew = Crew(
        agents=[blog_researcher, blog_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,  # Optional: Sequential task execution is default
        memory=True,
        cache=True,
        max_rpm=10,  # Reduced RPM to avoid possible rate limiting or resource issues
        share_crew=True
    )

    # Start the task execution process with enhanced feedback
    result = crew.kickoff(inputs={'topic': 'Live Crash Course On Graph Database With Langchain'})
    logging.info(f"Task execution result: {result}")

except Exception as e:
    logging.error(f"Error during crew execution: {e}")
