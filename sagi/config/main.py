import os
from pathlib import Path
from typing import Optional, Type

from pydantic import BaseModel
from pydantic_settings import SettingsConfigDict, BaseSettings, YamlConfigSettingsSource
from pydantic_settings_yaml import YamlBaseSettings


class DataConfig(BaseModel):
    root_dir_path: Path
    arc_v1_dir_path: Path
    arc_v2_dir_path: Path


class MainConfig(YamlBaseSettings):
    model_config = SettingsConfigDict(
        env_prefix = 'SAGI__',
        env_nested_delimiter='__',
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=False,
        nested_model_default_partial_update=True,
        secrets_dir='./',
        yaml_file=''
    )
    data: DataConfig

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings,
        env_settings,
        dotenv_settings,
        file_secret_settings,
    ):
        """
        Define the sources and their order for loading the settings values.

        Args:
            settings_cls: The Settings class.
            init_settings: The `InitSettingsSource` instance.
            env_settings: The `EnvSettingsSource` instance.
            dotenv_settings: The `DotEnvSettingsSource` instance.
            file_secret_settings: The `SecretsSettingsSource` instance.

        Returns:
            A tuple containing the sources and their order for
            loading the settings values.
        """
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls),
        )


def get_main_config(cfg_fpath: Optional[Path] = None, sfx: str = '') -> MainConfig:
    if cfg_fpath is None:
        if not sfx:
            sfx = os.getenv('SAGI_ENV', 'mac')
        if sfx and not sfx.startswith('.'):
            sfx = f'.{sfx}'
        cfg_fpath = Path('.').absolute()
        if not (cfg_fpath / 'config').exists():
            cfg_fpath = cfg_fpath.parent
        cfg_fpath /= f'config/main_config{sfx}.yaml'
    if cfg_fpath.exists():
        MainConfig.model_config['yaml_file'] = cfg_fpath
    main_cfg = MainConfig()
    return main_cfg

