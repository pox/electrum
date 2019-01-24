#!/usr/bin/env python3

import electrum
import json
from electrum.mnemonic import Mnemonic
from electrum.keystore import from_seed

COUNT = 4
seeds = [Mnemonic().make_seed() for _ in range(COUNT)]
keys = [from_seed(seed=seed, passphrase='') for seed in seeds]
for key in keys:
    print(json.dumps(key.dump(), indent=2))
