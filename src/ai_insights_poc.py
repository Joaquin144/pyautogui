from dotenv import load_dotenv

from src.core.generate_ai_insights import generate_ai_insights
from src.logger.config import setup_logger

log = setup_logger("ai_insights_poc")
load_dotenv()
insights = generate_ai_insights("""ABOUT

Experienced software developer with familiarity in design, installation and maintenance of software systems.
Equipped with a diverse and promising skill set and expertise with some of the cutting-edge development tools and
procedures. Tech-savvy full stack developer proficient in fundamental front-end languages and server-side
languages. Analytical and precise professional taking charge of front and back-end development. Have experience in
Python and Java which helped me to lead a team and earn STAR OF THE SPRINT recognition. Conversant with data
processing in Spark. Proficient with development and deployment of RDBMS and cloud tools such as MySQL, Oracle,
‘SQLServer, Snowflake, Azure, SFTP, AWS, GCP, etc as well as deployment of scalable data pipelines in Kubernetes
and Snowflake.

At the end of the day | aspire to be the happiest, the most successful and the best version of myself.
""")

log.info(f"insights = {insights}")
