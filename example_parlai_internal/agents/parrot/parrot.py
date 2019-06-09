#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
from parlai.core.torch_agent import TorchAgent, Output


class ParrotAgent(TorchAgent):
    def eval_step(self, batch):
        # for each row in batch, convert tensor to string
        return Output([str(row) for row in batch.text_vec])
