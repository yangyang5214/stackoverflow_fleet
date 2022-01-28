### jq

-s

```
➜  70886182 git:(main) ✗ cat example.txt
1111

111

222

3
➜  70886182 git:(main) ✗ cat example.txt | jq -s
[
  1111,
  111,
  222,
  3
]
```

### code

```shell
➜  70886182 git:(main) ✗ cat data.text 
{
  "id": "06b6751f-5125-4e48-b588-fcc8ff56004f",
  "dni": "78081181"
}
{
  "id": "4bdcf9e9-4a3e-4e13-963d-1270b94955dc",
  "dni": "77834021"
}

➜  70886182 git:(main) ✗ cat data.text | jq -s '.[] | {(.dni) : (.id)}'
{
  "78081181": "06b6751f-5125-4e48-b588-fcc8ff56004f"
}
{
  "77834021": "4bdcf9e9-4a3e-4e13-963d-1270b94955dc"
}

➜  70886182 git:(main) ✗ cat data.text | jq -s '.[]'                   
{
  "id": "06b6751f-5125-4e48-b588-fcc8ff56004f",
  "dni": "78081181"
}
{
  "id": "4bdcf9e9-4a3e-4e13-963d-1270b94955dc",
  "dni": "77834021"
}

➜  70886182 git:(main) ✗ cat data.text | jq -s      
[
  {
    "id": "06b6751f-5125-4e48-b588-fcc8ff56004f",
    "dni": "78081181"
  },
  {
    "id": "4bdcf9e9-4a3e-4e13-963d-1270b94955dc",
    "dni": "77834021"
  }
]
```