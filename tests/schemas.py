from pytest_schema import schema

company_schema = schema({
    "id": int,
    "name": str,
    "address": str,
    "zip": str,
    "country": str,
    "employeeCount": int,
    "industry": str,
    "marketCap": int,
    "domain": str,
    "logo": str,
    "ceoName": str
})

companies_schema = schema([company_schema])