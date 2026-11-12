.ONESHELL:
.PHONY: all beautiful black build clean commit-version dist echo isort jacobus py311 py312 py313 py314 py315 pypi rebase reset test toml_sorted_pyproject upload version
SHELL := /bin/zsh

all: beautiful commit-version

beautiful: isort black jacobus toml_sorted_pyproject

black: py311
	conda run -n py311 pip install 'black>=24.5,<26';
	conda run -n py311 black --line-length=79 . ;

build: beautiful py311
	conda run -n py311 pip install 'build>=1.3,<2';
	conda run -n py311 python -m build;

commit-version: py311
	git add -A;
	conda run -n py311 pip install 'toml_get>=1.1,<2';
	git commit --allow-empty "$$(conda run -n py311 python -m toml_get @make/toml_get.txt)";

clean:
	rm -fr 'dist/';

dist: clean build

echo:
	echo $(PARAMS);

isort: py311
	conda run -n py311 pip install 'isort>=6.0,<7';
	conda run -n py311 isort . ;

jacobus: py311
	conda run -n py311 pip install 'jacobus>=2.0,<3';
	conda run -n py311 python -m jacobus @make/jacobus.txt;

py311:
	conda run -n base python make/env.py py311 --python=3.11;

py312:
	conda run -n base python make/env.py py312 --python=3.12;

py313:
	conda run -n base python make/env.py py313 --python=3.13;

py314:
	conda run -n base python make/env.py py314 --python=3.14;

py315:
	conda run -n base python make/env.py py315 --python=3.15;

pypi: clean build upload

rebase:
	git rebase --empty=drop --interactive $(PARAMS);

reset:
	git reset HEAD~1;

test: dist py311
	mkdir dist/out/ ;
	conda run -n py311 pip install "style_checker>=0.1.5,<0.2";
	conda run -n py311 python -m style_checker -- "**/*.py" > dist/out/style_checker_out.txt 2> dist/out/style_checker_err.txt || true;
	conda run -n base python make/env.py test_raisefunction_mypy --python=3.11 --recreate >/dev/null;
	conda run -n test_raisefunction_mypy pip install dist/*.tar.gz >/dev/null;
	conda run -n test_raisefunction_mypy python make/run_introspection.py > dist/out/introspection_out.txt 2> dist/out/introspection_err.txt || true;
	conda run -n test_raisefunction_mypy pip install mypy >/dev/null;
	conda run -n test_raisefunction_mypy python -m mypy --exclude build --exclude dist --strict . > dist/out/mypy_dir_out.txt 2> dist/out/mypy_dir_err.txt || true;
	conda run -n test_raisefunction_mypy python -m mypy --strict -p raisefunction > dist/out/mypy_pkg_out.txt 2> dist/out/mypy_pkg_err.txt || true;
	conda run -n base python make/env.py test_raisefunction_tests --python=3.11 --recreate >/dev/null;
	conda run -n test_raisefunction_tests pip install dist/*.tar.gz >/dev/null;
	conda run -n test_raisefunction_tests python run_tests.py > dist/out/tests_out.txt 2> dist/out/tests_err.txt || true;
	zip -r dist/out.zip dist/out;

toml_sorted_pyproject: py311
	conda run -n py311 pip install 'toml_sorted>=2.2,<3';
	conda run -n py311 python -m toml_sorted @make/toml_sorted_pyproject.txt;

upload: py311
	conda run -n py311 pip install 'twine>=5.2,<7';
	conda run -n py311 twine upload 'dist/*';

version: all pypi
