import os
from dotenv import load_dotenv
from openai import OpenAI
import json
from time import time

def main():

    load_dotenv()

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ.get("OPENROUTER_API_KEY"),
        default_headers={
            "HTTP-Referer": "https://localhost:8888", 
            "X-Title": "E-Commerce Portfolio App",
        }    
    )

    note_system_prompt = """
    You are an AWS Examination expert and you are responsible in providing accurate and detailed answers to questions related to AWS services, architecture, and best practices. 
    Your responses should be clear, concise, and informative, catering to both beginners and experienced professionals in the field of cloud computing.
    """

    example_output_prompt = """
    Example output:

    ### Question: <topic covered>

    **Category:** <domain 1-4 of exam as provided> 
    **Review Bucket:** [ ] Bucket A (Term Mapping) | [ ] Bucket B (Missed Constraint) | [ ] Bucket C (Knowledge Gap) <Note: do not fill in the checkbox>

    A media company runs machine learning workloads in Amazon SageMaker AI for several internal business units. Each unit receives a predetermined AWS spending allowance every month, and resources are labeled with department-specific tags so that costs can be tracked separately. 

    Finance wants an automated way to notify each business unit **before** its **projected** monthly charges surpass its assigned spending limit, with **minimal administrative effort**.

    What solution should be implemented?

    * **A)** Create an AWS Cost Anomaly Detection monitor for each business unit. Scope each monitor by the cost allocation tags associated with the corresponding unit. Configure alert subscriptions to notify the unit when unusual spending patterns are detected during the month.
    * **B)** Configure a fixed budget in AWS Budgets for each business unit. Filter the budget by user-defined cost allocation tags assigned to each unit. Send an alert when forecasted monthly charges are expected to exceed the configured spending threshold.
    * **C)** Configure an auto-adjusting budget in AWS Budgets for each business unit. Filter the budget by AWS-generated cost allocation tags associated with each unit. Configure daily budget reports to provide updates on departmental spending.
    * **D)** Create a fixed budget in AWS Budgets for each business unit and filter the budget by user-defined cost allocation tags. Configure the budget to publish a notification to an Amazon SNS topic when actual monthly spending reaches the assigned limit. Subscribe an AWS Lambda function to the SNS topic to process the event and notify the corresponding business unit.

    ??? note "Click to reveal Answer & Explanation"
        **Correct Answer:** **B**

        #### Correct Option Analysis
        * **B is Correct:** AWS Budgets allows setting custom budget thresholds filtered by **user-defined cost allocation tags** (custom tags added by the team, like `Department: Marketing`). It natively supports alerts based on **forecasted** costs (notifying users *before* the limit is hit) without writing custom code or serverless infrastructure.

        #### Distractor Analysis
        * **A is Incorrect:** AWS Cost Anomaly Detection identifies unexpected spending spikes based on historical trends; it does not track spending against a fixed monthly budget cap or send alerts based on forecasted monthly totals.
        * **C is Incorrect:** Auto-adjusting budgets dynamically change based on spending patterns over time, which violates the requirement for a *predetermined monthly allowance*. Furthermore, custom tags applied by business units are *user-defined*, not *AWS-generated*.
        * **D is Incorrect:** This option uses *actual* spending (which alerts *after* the limit is reached instead of *before*) and introduces unnecessary operational overhead by building a custom Lambda + SNS processing pipeline when AWS Budgets natively supports email/SNS notifications.

        > **Key Takeaway:** For cost alerts **before** exceeding a limit, choose **AWS Budgets with Forecasted alerts**. Avoid custom Lambda pipelines when native AWS service alerts exist ("minimal operational effort").

    ??? warning "self-notes"
        <space for user to write self notes>

    ---
    """

    note_prompt = """
    You are provided with a unformatted exam question of AWS MLA-C02 exam.
    You are now responsible in turning it into markdown format and add explanation to correct and incorrect answers.
    Do not include extra explanation or opening/closing, only output the question and explanation in proper markdown format.
    The Answer and explanation should be in collapsible format as enclosed.
    """

    with open("./raw_question.txt", "r", encoding="utf-8") as f:
        question_raw_content = f.read()

    response = client.chat.completions.create(
        model="deepseek/deepseek-v4-pro-0813",
        messages=[
            {"role": "system", "content": note_system_prompt},
            {"role": "user", "content": note_prompt},
            {"role": "user", "content": example_output_prompt},
            {"role": "user", "content": "The raw question is as follows:"},
            {"role": "user", "content": question_raw_content},
        ],
        max_completion_tokens=4096
    )
    study_note_content = response.choices[0].message.content

    with open("./question_output.txt", "w", encoding="utf-8") as f:
        f.write(study_note_content)
    
    print("Exam question is converted to .md successfully.")

if __name__ == "__main__":
    main()
    