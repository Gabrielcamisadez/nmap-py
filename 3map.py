import asyncio

async def scan_network(ip_range):
    print(f"🔎 Iniciando scan na rede {ip_range}... Aguarde.")

    process = await asyncio.create_subprocess_exec(
        "nmap", "-sn", ip_range,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    if process.returncode == 0:
        print(f"⏳ Processando resultados: {ip_range}.")

        for line in stdout.decode().splitlines():
            if "Nmap scan report for" in line:
                ip = line.split()[-1].strip("()")
                print(f"🎯 Host ativo : {ip}")
                await asyncio.sleep(0.5) 
    else:
        print(f" Erro ao escanear a rede {ip_range}: {stderr.decode()}")

    print(f"🏆 Finish!")

async def main():
    ip_ranges = ["IP RANGE AQUI"]

    tasks = [scan_network(ip_range) for ip_range in ip_ranges]

    await asyncio.gather(*tasks)

asyncio.run(main())