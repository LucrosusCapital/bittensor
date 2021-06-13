# The MIT License (MIT)
# Copyright © 2021 Yuma Rao

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of 
# the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION 
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.

from os import name
import bittensor
import argparse
import copy

from . import metagraph_impl

class metagraph:
    
    def __new__(
            cls, 
            config: 'bittensor.config' = None,
            subtensor: 'bittensor.Subtensor' = None
        ) -> 'bittensor.Metagraph':
        r""" Creates a new bittensor.Metagraph object from passed arguments.
            Args:
                config (:obj:`bittensor.Config`, `optional`): 
                    bittensor.metagraph.config()
                subtensor (:obj:`bittensor.Subtensor`, `optional`): 
                    bittensor subtensor chain connection.
        """      
        if config == None: config = metagraph.config().metagraph
        config = copy.deepcopy(config)
        if subtensor == None:
            subtensor = bittensor.subtensor( config.subtensor )
        return metagraph_impl.Metagraph( subtensor = subtensor )

    @staticmethod   
    def config( config: 'bittensor.Config' = None, namespace: str = 'metagraph' ) -> 'bittensor.Config':
        if config == None: config = bittensor.config()
        metagraph_config = bittensor.config()
        bittensor.subtensor.config( metagraph_config )
        config[ namespace  ] = metagraph_config
        return config

    @staticmethod   
    def check_config( config: 'bittensor.Config' ):
        bittensor.subtensor.check_config( config.subtensor )