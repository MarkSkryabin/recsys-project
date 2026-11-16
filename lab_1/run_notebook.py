"""Execute the notebook using the current Python and a project-local kernel spec."""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
(ROOT / '.jupyter').mkdir(exist_ok=True)
local_runtime = ROOT / '.runtime'
use_local_runtime = sys.version_info[:2] == (3, 12) and local_runtime.is_dir()
if use_local_runtime:
    os.environ['PYTHONPATH'] = str(local_runtime) + os.pathsep + os.environ.get('PYTHONPATH', '')
os.environ['JUPYTER_PATH'] = str(ROOT / '.jupyter')
os.environ['JUPYTER_RUNTIME_DIR'] = str(ROOT / '.jupyter' / 'runtime')
os.environ['IPYTHONDIR'] = str(ROOT / '.jupyter' / 'ipython')
os.environ['MPLCONFIGDIR'] = str(ROOT / '.jupyter' / 'matplotlib')
os.environ['OMP_NUM_THREADS'] = '2'
os.environ['OPENBLAS_NUM_THREADS'] = '2'
os.environ['MKL_NUM_THREADS'] = '2'
if use_local_runtime:
    sys.path.insert(0, str(local_runtime))
import nbformat
from nbclient import NotebookClient

spec = ROOT / '.jupyter' / 'kernels' / 'recsys-hw1'
spec.mkdir(parents=True, exist_ok=True)
(spec / 'kernel.json').write_text(json.dumps({
    'argv': [sys.executable, '-m', 'ipykernel_launcher', '-f', '{connection_file}'],
    'display_name': 'Python 3 (RecSys HW1)', 'language': 'python',
}), encoding='utf-8')
notebook_paths = list(ROOT.glob('HW1_*.ipynb'))
if len(notebook_paths) != 1:
    raise ValueError('Ожидается один файл HW1_*.ipynb в папке lab_1')
path = notebook_paths[0]
nb = nbformat.read(path, as_version=4)
nbformat.validate(nb)

def start_cell(cell, cell_index, **kwargs):
    """Показать номер и начало кода очередной выполняемой ячейки."""
    if cell.cell_type == 'code':
        print(f'Executing cell {cell_index}: {cell.source.splitlines()[0][:90]}', flush=True)

def finish_cell(cell, cell_index, **kwargs):
    """Сохранить outputs после завершения каждой ячейки."""
    nbformat.write(nb, path)
    print(f'Saved cell {cell_index}', flush=True)

client = NotebookClient(nb, timeout=900, kernel_name='recsys-hw1',
                        resources={'metadata': {'path': str(ROOT)}},
                        on_cell_start=start_cell, on_cell_executed=finish_cell)
try:
    client.execute()
finally:
    nbformat.write(nb, path)
errors = [out for cell in nb.cells if cell.cell_type == 'code'
          for out in cell.outputs if out.output_type == 'error']
if errors:
    raise RuntimeError(f'Ошибки выполнения ноутбука: {errors}')
print(f'Completed: {path}', flush=True)
