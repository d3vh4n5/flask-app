



Para crear las variables de entorno en el servidor, pythonanywhere suguere hacer esto:

```bash
cd ~/my-project-dir
echo "export SECRET_KEY=sekritvalue" >> .env
echo "export OTHER_SECRET=somethingelse" >> .env
# etc
```

yo las cree en la carpeta raiz donde aparece la consola y funcionó.