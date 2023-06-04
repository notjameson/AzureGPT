# (Unofficial) Azure Pricing - ChatGPT Plugin

This is an open-source ChatGPT plugin that provides current pricing on Azure services.

**Note:** This plugin has not been submitted to ChatGPT so it can only be run locally through the "Develop your own plugin" feature. 
If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

> Thanks to the [Azure Retail Pricing API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices) for doing some heavy lifting.

## Screenshots
![Screenshot of 1st example](/media/AzurePricingDemoScreenshot1.png)

## Notes

- This is not an official plugin. I am developing this as an enthusiast, not an employee of Microsoft.
- You'll notice the regions, service families, and product names are manually added. This is because the Azure Retail Prices API doesn't publicly list the available values for those fields. I scripted the distinct values out.
- We take the top 5 configurations from the JSON response because ChatGPT plugins have a limit on content length. There are ways to tackle this that I'd explore in the future.
- Yes, the math can sometimes be off. ChatGPT is still in beta when it comes to calculations. The real alpha and value (IMO) comes from building out a solution while discussing price and tradeoffs, with an AI, in the same app.
- As of now, it's one service per request. ChatGPT can decide to make any number of requests.

## Setup

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

To run the plugin, enter the following command:

```bash
python serve.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5001` since this is the URL the server is running on locally, then select "Find manifest file".

## Prompt examples

Continuing from the first example above
![Screenshot of 2nd example](/media/AzurePricingDemoScreenshot2.png)

![Screenshot of 3rd example](/media/AzurePricingDemoScreenshot3.png)

1. I've got about 70,000 photos from my phone that I want to store in Azure. What's the cheapest way for me to upload them, and how much will it cost? I'd like to keep them in a Central US data center.
2. What are the free tier options for x service?
3. What are cheaper alternatives to x service?
4. I want to build an Azure Function that does x. How much would that cost per month to run? Assume y.