import subprocess

from celery import shared_task
from django.core.mail import mail_admins

from orchestrator.models import ExecutionLog, Script


@shared_task
def run_script(script_id: int) -> dict[str, object]:
    script = Script.objects.get(id=script_id)
    try:
        result = subprocess.run(
            ["/user/bin/env python", script.path],
            capture_output=True,
            text=True,
            timeout=300,
            check=True,
            shell=False,
        )

        log = ExecutionLog.objects.create(
            script=script,
            return_code=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
            success=(result.returncode == 0),
        )

    except ValueError as e:
        log = ExecutionLog.objects.create(script=script, stderr=str(e), success=False)

        mail_admins(subject=f"Falha critica ao executar script: {script.name}", message=str(e))

        return {"log_id": log.id, "error": str(e)}

    else:
        if result.returncode != 0:
            mail_admins(
                subject=f"Erro ao executar script: {script.name}",
                message=f"""
Script: {script.name}
Path: {script.path}
Erro: {result.stderr}
Codigo de Retorno: {result.returncode}
""",
            )

        return {
            "log_id": log.id,
            "stdout": result.stdout,
            "strerr": result.stderr,
            "returncode": result.returncode,
        }
