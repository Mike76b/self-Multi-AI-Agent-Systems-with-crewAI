# main.py
from crewai import Crew, Agent, Task

agent = Agent(
    role="Data analyst",
    goal="Extract insights from sales data",
    backstory="Experienced with pandas and visualization.",
)

task = Task(
    description="Load the CSV, compute monthly totals, and plot a bar chart.",
    agent=agent,
)

crew = Crew(tasks=[task])
results = crew.kickoff()

print(results)
