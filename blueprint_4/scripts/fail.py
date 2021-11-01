from cloudify.exceptions import NonRecoverableError


def main():
    raise NonRecoverableError('Failed.')


if __name__ == "__main__":
    main()
