# API - CAPSTONE - NOTE TIME

O Note time é uma aplicação RESTful, para que registrar o tempo de estudos, categoria de estudos, entrar em grupos, escrever comentarios e guardar seus estudos.

#### URL DA API

https://note-time-api.herokuapp.com/api/

# Enpoints

A API tem 6 endpoints diferentes, para criação do lead, atualização, deletar e listar todos os leads.

**Nehuma rota necessita de autenticação**

## 1.User

---

<br />

## Register

<br />

`POST/user/register`

```json
{
  "name": "matheus",
  "email": "matheus1234@gmail.com",
  "password": "matheus123"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
  "name": "matheus",
  "email": "matheus1234@gmail.com"
}
```

---

## Login

<br />

`POST/user/login`

```json
{
  "email": "matheus1234@gmail.com",
  "password": "matheus123"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0NjQ0NzU5MiwianRpIjoiYjZlNTk5YzItODZmMS00YmQzLTg4MWMtZmFiNmYwZTE5MTVjIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJuYW1lIjoibWF0aGV1cyIsImVtYWlsIjoibWF0aGV1czEyM0BnbWFpbC5jb20iLCJhY3Rpdml0eSI6W119LCJuYmYiOjE2NDY0NDc1OTIsImV4cCI6MTY0NjQ0ODQ5Mn0._HmYLfMkE0USVhwSyR_F4VZbJmevDKeU3ze2-yxD0do"
}
```

---

## Update

<br />

**Rota necessita de autenticação**

`PATCH/user`

```json
{
  "email": "matheus12345@gmail.com"
}
```

Requisição **bem sucedida** , sem retorno.

`STATUS 204 - NO CONTENT`

---

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/user`

{}

Requisição **bem sucedida** , sem retorno.

`STATUS 204 - NO CONTENT`

---

## Get

<br />

**Rota necessita de autenticação**

`GET/user`

```json
{}
```

Requisição **bem sucedida**, retorna a seguinte resposta.

```json
{
  "name": "Laudemir Junior",
  "timer_general": "0:00:15",
  "image": [
    {
      "url_image": "https://note-time-api.herokuapp.com/api/image/037650a1-e3f0-4bfe-88f4-bc08cc7b7d40"
    }
  ],
  "activity": [
    {
      "id": "8cf162d7-ba76-4de9-a436-5414064006e7",
      "timer_total": "00:00:02",
      "timer_init": null,
      "favorite": false,
      "category": {
        "name": "Vue"
      },
      "card": []
    },
    {
      "id": "324fd6f6-ad6f-493f-87ff-795462b924b8",
      "timer_total": "00:00:13",
      "timer_init": null,
      "favorite": true,
      "category": {
        "name": "React"
      },
      "card": [
        {
          "id": "ea5ae3ac-b221-4dc3-aad2-08d156548207",
          "title": "Fazer rota post",
          "description": "Fazendo a rotinha marota"
        }
      ]
    }
  ]
}
```

`STATUS 200 - OK`

---

## Get All

<br />

**Rota necessita de autenticação**

`GET/user/all`

```json
{}
```

Requisição **bem sucedida**, retorna a seguinte resposta.

```json
 {
    "name": "Natan",
    "timer_general": "1:44:31",
    "image": [
      {
        "url_image": "https://note-time-api.herokuapp.com/api/image/8265f737-e5cc-4c1d-828e-c41b25cf3683"
      }
    ]
  },
  {
    "name": "Laudemir Junior",
    "timer_general": "0:00:15",
    "image": [
      {
        "url_image": "https://note-time-api.herokuapp.com/api/image/037650a1-e3f0-4bfe-88f4-bc08cc7b7d40"
      }
    ]
  },
  {
    "name": "John1",
    "timer_general": "00:00:00",
    "image": []
  }
```

`STATUS 200 - OK`

---

## Post add Group

<br />

**Rota necessita de autenticação**

`POST/user/group/<group_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
  "messsage": "User registered to group"
}
```

---

<br />
<br />

## 2. Image

---

## Post

<br />

**Rota necessita de autenticação**

`POST/image`

```json
{
  "image": "file.jpg"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
  "id": "9b192342-9b35-4b03-9e58-a0f161c2a524"
}
```

---

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/image`

```json
{
  "image": "file.jpg"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
  "id": "9b192342-9b35-4b03-9e58-a0f161c2a524"
}
```

---

## Get

<br />

**Rota necessita de autenticação**

`GET/image/<image_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
  "image": "file.jpg"
}
```

---

## Delet

<br />

**Rota necessita de autenticação**

`DELETE/image/<image_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 204 - NO CONTENT`

```json
{}
```

---

<br />
<br />

## 3. Group

---

## Get

<br />

**Rota necessita de autenticação**

`GET/group`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
[
  {
    "id": "d5541e63-de5b-4c2c-9e2d-391ac27e308c",
    "title": "Grupo Do Bolinha23",
    "privacy": true
  },
  {
    "id": "4e594719-0859-4fca-a9b0-255723051f7c",
    "title": "Meu Time Lindo",
    "privacy": false
  },
  {
    "id": "2c4e484a-e5eb-47bd-aa4f-454e843f4859",
    "title": "Grupo Do Bolinha234",
    "privacy": false
  }
]
```

---

## Post

<br />

**Rota necessita de autenticação**

`POST/group`

```json
{
  "title": "grupo do bolinha23"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
  "id": "5cf8c308-224f-47f1-8086-03f009a7d726",
  "title": "grupo do bolinha23",
  "privacy": false
}
```

---

## Update

<br />

**Rota necessita de autenticação**

`PATCH/group/<group_id>`

```json
{
  "privacy": true
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
  "id": "d5541e63-de5b-4c2c-9e2d-391ac27e308c",
  "title": "Grupo Do Bolinha23",
  "privacy": true
}
```

---

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/group/<group_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 204 - NO CONTENT`

```json
{}
```

---

<br />
<br />

## 4. Comment

---

## Get

<br />

**Rota necessita de autenticação**

`GET/<group_id>/comment`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
[
  {
    "id": "d460729c-6519-41ad-a7e5-1c4532e303d3",
    "hour": "Mon, 07 Mar 2022 15:23:54 GMT",
    "comment": "Comentários oi",
    "user_id": "a60e0ea3-7aa3-4632-a8ef-bda4edf1eb13",
    "group_id": "d5541e63-de5b-4c2c-9e2d-391ac27e308c"
  },
  {
    "id": "bb9b18a0-e9d4-4801-837c-363a9d6c1ae4",
    "hour": "Mon, 07 Mar 2022 15:23:54 GMT",
    "comment": "Só da bom aqui",
    "user_id": "f333cdd0-a1e1-43a6-a963-ae96d35c0c02",
    "group_id": "d5541e63-de5b-4c2c-9e2d-391ac27e308c"
  },
  {
    "id": "e566a420-6162-4c75-969e-f5bd1aac65de",
    "hour": "Mon, 07 Mar 2022 16:28:29 GMT",
    "comment": "Comentário oi",
    "user_id": "f333cdd0-a1e1-43a6-a963-ae96d35c0c02",
    "group_id": "d5541e63-de5b-4c2c-9e2d-391ac27e308c"
  }
]
```

---

## Post

<br />

**Rota necessita de autenticação**

`POST/<group_id>/comment`

```json
{
  "comment": "um bom comentário"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
  "id": "36127d52-67dc-45d9-8b8d-192e859f988f",
  "hour": "Mon, 07 Mar 2022 21:58:58 GMT",
  "comment": "um bom Comentario",
  "user_id": "a60e0ea3-7aa3-4632-a8ef-bda4edf1eb13",
  "group_id": "d5541e63-de5b-4c2c-9e2d-391ac27e308c"
}
```

---

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/<group_id>/comment/<comment_id>`

```json
{
  "comment": "comentario legal"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
  "id": "36127d52-67dc-45d9-8b8d-192e859f988f",
  "hour": "Mon, 07 Mar 2022 21:58:58 GMT",
  "comment": "Comentario legal",
  "user_id": "a60e0ea3-7aa3-4632-a8ef-bda4edf1eb13",
  "group_id": "d5541e63-de5b-4c2c-9e2d-391ac27e308c"
}
```

---

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/<group_id>/comment/<comment_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 204 - NO CONTENT`

```json
{}
```

---

<br/>
<br/>

## 5. Activity

---

## Post

<br />

**Rota necessita de autenticação**

`POST/activity`

```json
{
  "name": "CSS"
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
  "id": "3ae4ac42-04bb-4c23-b9f5-c58853b00932",
  "timer_total": "00:00:00",
  "timer_init": null,
  "favorite": false,
  "category": {
    "name": "Css"
  },
  "card": []
}
```

---

## Post Play

<br />

**Rota necessita de autenticação**

`POST/activity/<activity_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
  "timer_init": "2022-03-07 23:47:58",
  "timer_total": "00:00:00"
}
```

---

## Post Pause

<br />

**Rota necessita de autenticação**

`POST/activity/<activity_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
  "timer_total": "00:00:33"
}
```

---

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/activity/<activity_id>`

```json
{
  "favorite": true
}
```

Requisição **bem sucedida** sem retorno.

`STATUS 200 - OK`

```json
{}
```

---

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/activity/<activity_id>`

```json
{}
```

Requisição **bem sucedida** sem retorno.

`STATUS 204 - NO CONTENT`

```json
{}
```

---

## Get

<br />

**Rota necessita de autenticação**

`GET/activity/<activity_id>`

```json
{}
```

Requisição **bem sucedida** sem retorno.

`STATUS 200 - OK`

```json
{
  "id": "c681ac4b-c389-499f-ba03-78abd2a138a8",
  "timer_total": "00:00:00",
  "timer_init": null,
  "favorite": false,
  "category": {
    "name": "Css"
  },
  "card": []
}
```

---

<br />
<br />

## 6. Card

---

## Post

<br />

**Rota necessita de autenticação**

`POST/card/<acivity_id>`

```json
{
  "title": "Estudo Css 1",
  "description": "Estudando a parte inicila de css."
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 201 - CREATED`

```json
{
  "id": "2600a4c1-7ebd-4f5d-a7f3-d4f7a28a7f4b",
  "title": "Fazer rota post",
  "description": "Fazendo a rotinha marota"
}
```

---

## Patch

<br />

**Rota necessita de autenticação**

`PATCH/card/<acivity_id>`

```json
{
  "title": "Estudo Css 2",
  "description": "Estudando a parte final de css."
}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{}
```

---

## Delete

<br />

**Rota necessita de autenticação**

`DELETE/card/<acivity_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{}
```

---

## Get

<br />

**Rota necessita de autenticação**

`GET/card/<acivity_id>`

```json
{}
```

Requisição **bem sucedida** retorna a seguinte resposta:

`STATUS 200 - OK`

```json
{
  "id": "2600a4c1-7ebd-4f5d-a7f3-d4f7a28a7f4b",
  "title": "Estudo Css 2",
  "description": "Estudando a parte final de css."
}
```

---
