# Background
Under a cooperative agreement with the U.S. Department of Agriculture (USDA), the [George Washington University Regulatory Studies Center (RSC)](https://regulatorystudies.columbian.gwu.edu/) conducted research analyzing public comments to inform agency regulatory reform efforts in the United States. A group of faculty members and researchers affiliated with the GW Regulatory Studies Center contributed to the research project, and subject matter experts at the USDA Office of the Chief Economist provided technical advice. The research report is available at: https://regulatorystudies.columbian.gwu.edu/putting-food-table-agriculture-and-regulation.

In this research, we (the RSC research team) developed Python code to retrieve, clean, and analyze data of public comments. We share the code in this reporsitory. The goal is to provide code that can be easily modified for use in other research using public comments.

# Retrieving public comments from Regulations.gov
## Regulations.gov API
[Regulations.gov](https://www.regulations.gov/) is a central portal for public users to access U.S. federal regulatory materials and submit comments on proposed regulations. It was launched by the [eRulemaking Program](https://www.regulations.gov/aboutProgram) in January 2003. Today, nearly 300 federal agencies post an average of 8,000 regulations per year, among which the majority receive comments and share them on Regulations.gov, while others accept and post comments via other online platforms (e.g., Surface Transportation Board).

Regulations.gov offers all its public data in machine readable format via an [API (Application Programming Interface)](https://www.regulations.gov/apiOverview), which allows users to search and retrieve data on public submissions and other regulatory materials in a machine readable format. All the content that can be obtained using the regular search function on Regulations.gov is available in json or xml format if an equivalent [API query](https://regulationsgov.github.io/developers/console/) is used. This includes the full text of comments and rules, as well as their metadata such as agency name, commenter name, publication date, etc.

For detailed description of Regulations.gov API, visit: https://regulationsgov.github.io/developers/.

### How to request a API key