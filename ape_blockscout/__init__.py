from ape import plugins


@plugins.register(plugins.ExplorerPlugin)
def explorers():
    from ape_blockscout.explorer import Blockscout
    from ape_blockscout.utils import NETWORKS

    for ecosystem_name in NETWORKS:
        for network_name in NETWORKS[ecosystem_name]:
            yield ecosystem_name, network_name, Blockscout
            yield ecosystem_name, f"{network_name}-fork", Blockscout


@plugins.register(plugins.Config)
def config_class():
    from ape_blockscout.config import BlockscoutConfig

    return BlockscoutConfig

def __getattr__(name: str):
    if name == "NETWORKS":
        from ape_blockscout.utils import NETWORKS

        return NETWORKS

    elif name == "Blockscout":
        from ape_blockscout.explorer import Blockscout

        return Blockscout

    elif name == "BlockscoutConfig":
        from ape_blockscout.config import BlockscoutConfig

        return BlockscoutConfig

    else:
        raise AttributeError(name)


__all__ = ["NETWORKS", "Blockscout", "BlockscoutConfig"]