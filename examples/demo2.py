import logging
import coloredlogs
import indentedlogs

fmt = '{asctime} {levelname:<8} {filename:>3}:{lineno:<3} {name:>10} {message}'
coloredlogs.install(level='DEBUG', fmt=fmt, style='{')
indentedlogs.install()  # must be called after coloredlogs
log = logging.getLogger()

def bump_version():
    pass


def configure():
    log.debug(f"Collecting parameters")
    log.debug(f"Ask for confirmation")
    log.info(f"Save configuration")


def select_target():
    log.warning(f"Default target selected")


def prepare():
    log.debug(f"Bump version")
    bump_version()
    log.debug(f"Generate configuration")
    configure()
    log.debug(f"Select target")
    select_target()


def call_compiler():
    log.debug(f"Preprocess sources")
    log.info(f"Compile sources")


def call_linker():
    log.info(f"Link objects")


def build_executable():
    # Note that callables that don't invoke logging
    # don't create additional indentation
    call_compiler()
    call_linker()


def build_package():
    log.warning(f"Symbols will be removed")
    log.debug(f"Strip binary")
    log.debug(f"Add meta data")
    log.debug(f"Create archive")


def upload_package():
    pass


def release_app():
    log.debug(f"Prepare")
    prepare()
    log.info(f"Build executable")
    build_executable()
    log.info(f"Build package")
    build_package()
    log.info(f"Upload package")
    upload_package()


release_app()
