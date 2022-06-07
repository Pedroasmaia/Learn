# Azure CLI

## Autenticando

- Documentação: [https://docs.microsoft.com/pt-br/cli/azure/authenticate-azure-cli](https://docs.microsoft.com/pt-br/cli/azure/authenticate-azure-cli)

- Usuário comum:

    ~~~powershell
    az login -u <username> -p <password> 
    ~~~

## Subscriptions

- Listar Subscriptions

    ~~~powershell
    az account list
    ~~~

- Definir Subscription Ativa

    Aceita receber -n e/ou -s

    ~~~powershell
    az account set -n <name> -s <id_subscription>
    ~~~

- Mostrar Subscription Ativa

    Aceita receber -n e/ou -s

    ~~~powershell
    az account show
    ~~~
