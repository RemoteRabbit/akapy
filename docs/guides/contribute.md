### Prerequisites
- [pre-commit](https://pre-commit.com/)
- [Poetry](https://python-poetry.org/)

### Pull the Repo

#### My way

```sh
mkdir -p $HOME/repos/open-source
git clone https://github.com/RemoteRabbit/akapy.git >> $HOME/repos/open-source
tms $HOME/repos/open-source/akapy
```

#### General Way
```sh
git clone https://github.com/RemoteRabbit/akapy.git
```


#### Setup pre-commit

Once you have pre-commit installed and the repo pulled down to your local machine, `cd` into it. Once in run:

```sh
pre-commit install
```

After that you can continue on and when you go to commit any changes you'll see some base tests run beforehand that you'll want to make sure are in
working order before pushing the change up.
