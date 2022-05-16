# 1° Challenge de Dados -  Alura
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

<center>
  <img src="https://i.imgur.com/jn7km8o.png">
</center>

A Alura Voz é uma empresa de telecomunicação que nos contratou para atuar como cientistas de dados na equipe de vendas. Logo na primeira semana, a liderança nos informa que é muito necessário realizar um estudo quanto ao Churn da empresa. É explicado que o churn indica se um cliente cancelou ou não o contrato com a empresa, e também que, nos casos de perda do cliente a empresa também perde faturamento, o que ocasiona prejuizos na receita final.

Desse modo, nossa liderança informa que temos 4 semanas para buscar uma alternativa que possa minimizar a saída de clientes e nos entrega um conjunto de dados da Alura Voz que contém diversas informações sobre os clientes e também informa se eles deixaram ou não a empresa.

Sabemos que, antes de pensar em qualquer alternaiva, é preciso entender as informações que recebemos e, após uma pequena reunião, concluímos que na primeira semana nós nos dedicaríamos a entender o banco de dados, descobrir os tipos de dados, verificar a existencia de valores incoerentos e corrigi-los caso seja necessário.

## Semana 1 - Limpeza dos dados

### Dados

Ao observar a [Base de dados da Alura Voz](https://github.com/sthemonica/alura-voz/blob/main/Dados/Telco-Customer-Churn.json), verificamos que essa é uma base disponibilizada via API em formato JSON com várias camandas de dados.

Junnto a esses dados também foi disponibilizado o [dicionário dos dados](https://github.com/sthemonica/alura-voz/blob/main/dicionario.md) que nele contém todas as informações sobre as colunas do banco de dados.

Nela, além da informação se o cliente deixou ou não a empresa, também contém:

<b>Cliente:</b>
 
* `gender`: gênero (masculino e feminino)
* `SeniorCitizen`: informação sobre um cliente ter ou não idade igual ou maior que 65 anos
* `Partner`: se o cliente possui ou não um parceiro ou parceira
* `Dependents`: se o cliente possui ou não dependentes

<b>Serviço de telefonia</b>


 * `tenure`: meses de contrato do cliente
 * `PhoneService`: assinatura de serviço telefônico
 * `MultipleLines`: assisnatura de mais de uma linha de telefone
 

<b>Serviço de internet</b>


 * `InternetService`: assinatura de um provedor internet
 * `OnlineSecurity`: assinatura adicional de segurança online
 * `OnlineBackup`: assinatura adicional de backup online
 * `DeviceProtection`: assinatura adicional de proteção no dispositivo
 * `TechSupport`: assinatura adicional de suporte técnico, menos tempo de espera
 * `StreamingTV`: assinatura de TV a cabo
 * `StreamingMovies`: assinatura de streaming de filmes


<b>Contrato</b>


 * `Contract`: tipo de contrato
 * `PaperlessBilling`: se o cliente prefere receber online a fatura
 * `PaymentMethod`: forma de pagamento
 * `Charges.Monthly`: total de todos os serviços do cliente por mês
 * `Charges.Total`: total gasto pelo cliente

Tendo essas informações entendemos nossos dados e, assim, podemos realizar uma análise mais técnica, buscando entender JSON, os dados e realizar o tratamento deles.

Todo o desenvolvimento feito na nossa 1° semana pode ser observado no [notebook semana 1](https://github.com/sthemonica/alura-voz/blob/main/1-Limpeza%20dos%20dados/limpeza.ipynb).

#alura #alurachallengedatascience1


### Contatos:

#### Sthefanie, Ana Clara, Bruno, João e Mirla 
<div>
<a href="https://www.linkedin.com/in/sthefanie-monica/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>  
<a href="https://www.linkedin.com/in/anaclara-amioto/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
<a href="https://www.linkedin.com/in/bruno-raphaell-alves-de-matos/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
<a href="https://www.linkedin.com/in/joaovmiranda/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
<a href="https://www.linkedin.com/in/mirla-costa/" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>   
</div>