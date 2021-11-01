from cloudify import ctx
from cloudify.exceptions import NonRecoverableError


def main():
    ctx.logger.info('Fixed!')


if __name__ == "__main__":
    main()
