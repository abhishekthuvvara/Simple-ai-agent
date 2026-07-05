import pandas as pd

# Load the Excel file
df = pd.read_excel("simple-ai-agent/Dataset for Data Analytics.xlsx")

print("🤖 Welcome to the Order Chatbot!")
print("Type 'exit' to quit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("🤖 Hello! Ask me about the dataset.")

    elif user == "total orders":
        print("🤖 Total Orders:", len(df))

    elif user == "total sales":
        print("🤖 Total Sales: ₹", df["TotalPrice"].sum())

    elif user == "payment methods":
        print("🤖 Payment Methods:")
        print(df["PaymentMethod"].unique())

    elif user == "pending orders":
        pending = df[df["OrderStatus"].str.lower() == "pending"]
        print("🤖 Pending Orders:", len(pending))

    elif user == "products":
        print("🤖 Products:")
        print(df["Product"].unique())

    elif user == "exit":
        print("🤖 Goodbye!")
        break

    else:
        print("🤖 Sorry! I can answer only these questions:")
        print("- total orders")
        print("- total sales")
        print("- payment methods")
        print("- pending orders")
        print("- products")
        print("- exit")