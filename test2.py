from typing import Annotated, TypedDict

from langchain_upstage import ChatUpstage
from langgraph.graph.message import add_messages
from langchain_core.messages import ToolMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class State(TypedDict):
    messages: Annotated[list, add_messages]
    found: bool


tools = [
    to_paper_search_agent,
    to_download_and_parse_paper_agent,
    to_retrieve_paper_content_to_answer_question_agent,
]

llm = ChatUpstage()
llm = llm.bind_tools(tools)


def chatbot(state: State):
    messages = state["messages"]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            MessagesPlaceholder(variable_name="messages"),
        ]
    )

    chain = prompt | llm
    response = chain.invoke({"messages": messages})

    return {"messages": [response]}
