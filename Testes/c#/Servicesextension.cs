using System;
using System.ServiceProcess;

namespace ServiceScanner
{
    class Program
    {
        static void Main(string[] args)
        {
            ServiceController[] services = ServiceController.GetServices();

            foreach (ServiceController service in services)
            {
                Console.WriteLine($"Service Name: {service.ServiceName}");
                Console.WriteLine($"Display Name: {service.DisplayName}");
                Console.WriteLine($"Status: {service.Status}");

                // Aqui você pode adicionar lógica para verificar se o serviço é malicioso
                bool isMalicious = CheckForMaliciousService(service.ServiceName);

                if (isMalicious)
                {
                    Console.WriteLine("ALERT: Malicious service detected!");
                }

                Console.WriteLine("--------------------------------------------------");
            }
        }

        // Função para verificar se o serviço é malicioso (exemplo)
        static bool CheckForMaliciousService(string serviceName)
        {
            // Aqui você pode implementar suas regras de verificação de serviços maliciosos
            // Por exemplo, comparar o nome do serviço com uma lista de serviços maliciosos conhecidos
            // Se o serviço estiver na lista, retorne true, caso contrário, retorne false.
            // Lembre-se de que a detecção de serviços maliciosos é complexa e exige mais análises do que isso.

            // Exemplo de implementação:
            string[] maliciousServices = { "badservice1", "badservice2" };

            foreach (string maliciousService in maliciousServices)
            {
                if (serviceName.Equals(maliciousService, StringComparison.OrdinalIgnoreCase))
                {
                    return true;
                }
            }

            return false;
        }
    }
}
