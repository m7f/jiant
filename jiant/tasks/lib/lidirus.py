from dataclasses import dataclass

from . import terra


@dataclass
class Example(terra.Example):
    pass


@dataclass
class TokenizedExample(terra.Example):
    pass


@dataclass
class DataRow(terra.DataRow):
    pass


@dataclass
class Batch(terra.Batch):
    pass


class LiDiRusTask(terra.TerraTask):
    def get_train_examples(self):
        raise RuntimeError("This task does not support training examples")

    def get_val_examples(self):
        raise RuntimeError("This task does not support validation examples")
