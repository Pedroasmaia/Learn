# Terraform no Azure Infraestrutura como Código e DevOps
- **Instrutor:** [Higor Barbosa](https://www.linkedin.com/in/higor-barbosa/)
- **Plataforma:** [Udemy](https://www.udemy.com/course/terraformazure/)

# Módulo 1 | Introdução ao IaC e Azure Cloud:

## Principais recursos:

### Analytics:

- **Azure Databricks:** É um serviço de analise rapida e colaborativa, baseado no *Apache Spark* voltado para *AI* e *Big data*
- **Azure Stream Analytics:** É um serviço de analise em tempo real sobre demanda para *IoT*
- **Azure Datafactory** É um *ETL* na nuvem

### Armazenamento:

- **Storage Account:** É um serviço de armazenamento altamente disponível e redundante.
- **Blob Storage:** É um serviço de armazenamento para dados não estruturados.

### Databases:

- **SQL SERVER:** SQL servers em máquinas virtuais.
- **Azure Cosmos DB:** Serviço de dados multi-modelo distribuído globalmente
- **Azure Cache for Redis:** Armazenamento de dados em memoria compatível com software livre e totalmente gerenciado
- **Armazenamento de tabelas:** Repositório de chave-valor *NoSQL* semi estruturados

### Computação:

- **Máquinas virtuais:** O Nome é autoexplicativo.
- **VMSS:** Conjunto de escalonamentos de Máquinas virtuais
- **Azure Function:** Criar aplicativos com arquitetura *Serveless*
- **App Sevice:** Aplicativos de Nuvem
- **Batch:** Agendamento de trabalho
- **AKS:** Kubernetes

## Regiões Azure e Resource Group(Grupo de Recursos):

- **Conceito de Região do Azure:** É um conjunto de Datas Centers implantados dentro de um perímetro, de latência definida e conectada por uma rede regional dedicada de baixa latência.
    - [Regiões disponíveis](https://docs.microsoft.com/pt-br/azure/availability-zones/az-overview)
-**Conceito de Grupo de Recurso:** É um agrupamento de *recursos*(serviços), para controla-los melhor.
    - Os *recursos* de um *grupo de recursos* deve compartilhar o mesmo ciclo de vida.
    - Os *recursos* podem ser adicionados ou removidos dos *grupos de recursos*, a qualquer momento, mas nunca estar em dois grupos ao mesmo tempo.
    - Os *recursos* podem estar em *regiões* diferentes mesmo estando no mesmo *grupo de recursos*.
    - *Recursos* de grupos diferentes podem interagir entre sí. 
- **Tags:** Categorização dos recursos.
- **Locks:** Bloqueios em cada recursos (ex: bloquear exclusão acidental).
- **IAM:** Controle de Acesso por recurso.

## Infraestrutura como Código IAC:

- É um script para provisionamento de recursos
- Automatizando o provisionamento, entregando os recursos mais rápidos
- Validar a qualidade da nossa infraestrutura



## Como provisionar os recursos no Azure:

- Portal do Azure
- Deploy via *PowerShell*
- Azure CLI (Comand Line Interface)
- Azure Cloud Shell
- ARM (AZURE RESOURCE MANAGER) - IAC
- Terraform - IAC
- [API REST do Azure](https://docs.microsoft.com/en-us/rest/api/) via requisições.

## Comparando ARM com Terraform:

### **ARM:**

- **Vantagens:**
    - É possível criar recursos a partir de outros já provisionados pelo portal
    - *Azure Quickstart templates* Templates disponíveis no github
- **Desvantagens:**
    - Ruim para leitura humana
    - Funciona somente na Azure


## Infraestrutura: Provisionamento x Configurações

- Provisionamento: Criar, alterar e excluir recursos.
- Configurações: Terraform não faz, mas é bom conhecer o *Ansible*

# Módulo 2 | Terraform - Básico:

## Terraform:

- Significa de *Modelar a Terra*
- Ferramenta declarativa de provisionamento automatizado
- Lançamento em Maio/2014
- Linguagem própria chamada *HCL*
- Extensão .tf
- Multiprovedor
- Curva de aprendizagem baixa
- Foi desenvolvido usando *GO*

## Como o Terraform funciona:

O Terraform contem dois componentes principais:

- **Core:** O Centro do terraform, e temos duas entradas principais:
    - As *configurações* que damos a ele, do que será configurado na nossa infraestrutura
    - E o *State* o estado atual do setup
    ~~~terraform
        terraform plan
        #É aqui que ele faz a comparação do que vai ser alterado
    ~~~
- **Providers:** Os provedores que convertem o nosso código em serviços