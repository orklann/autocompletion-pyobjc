# autocompletion-pyobjc
Autocompletion files generator for PyObjc

### How to use

Need to install `virtualenv` with `pip` before these steps

```
virtualenv -p `which python3` autocomplete

source example/bin/activate.fish # <= for Fish shell, activate.sh for Bash shell

pip install pyobjc

python3 main.py > autocomplete.py
```

###### I use `autocomplete.py` in Atom editor
