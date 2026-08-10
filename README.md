Sistema Final: Bot de Trading LATAM - Automatización y Cloud DevOps
Este repositorio contiene la solución completa de infraestructura como código, pipelines de CI/CD, despliegue en Kubernetes y monitoreo para un sistema de trading automatizado orientado al mercado de América Latina.

📁 Estructura del Repositorio
El proyecto está organizado de manera modular y limpia para facilitar su despliegue y auditoría:

Plaintext
sistema-final/
├── .github/workflows/      # Pipelines de CI/CD (GitHub Actions)
├── backend/                # Código fuente de la aplicación, Dockerfile y dependencias
├── k8s/                    # Manifiestos de Kubernetes (Deployments, HPA, Ingress, Postgres)
├── nginx/                  # Configuración del proxy inverso Nginx
├── prometheus/             # Manifiestos y configuración de Prometheus y Grafana
├── sistema-bot/            # Configuración de Helm Charts y plantillas complementarias
└── terraform/              # Infraestructura como Código (VPC, EKS Cluster, Nodos)
🚀 Tecnologías y Herramientas Utilizadas
Cloud Provider: Amazon Web Services (AWS)

Infraestructura como Código (IaC): Terraform (v20.x y módulos oficiales de VPC y EKS)

Orquestación: Kubernetes (EKS) con auto-escalado horizontal (HPA)

CI/CD: GitHub Actions

Contenedores: Docker (con optimización multi-stage builds)

Monitoreo: Prometheus y Grafana

🛠️ Instrucciones de Despliegue y Ejecución
1. Prerrequisitos Locales
Asegúrate de tener instaladas las siguientes herramientas en tu entorno de trabajo:

aws-cli configurado con tus credenciales de IAM.

terraform (versión 1.x o superior).

kubectl para la gestión del clúster de Kubernetes.

2. Provisionamiento de Infraestructura (Terraform)
Dirígete a la carpeta de Terraform para levantar la red (VPC) y el clúster de EKS en AWS:

Bash
cd terraform
terraform init
terraform apply --auto-approve
Una vez finalizado, configura tu contexto local para interactuar con el clúster:

Bash
aws eks update-kubeconfig --name cluster-bot-trading --region us-east-2
3. Despliegue de Manifiestos en Kubernetes
Desde la raíz del proyecto, aplica los manifiestos de la aplicación y el auto-escalador (HPA):

Bash
kubectl apply --validate=false -f ./k8s/backend-deployment.yaml
kubectl apply --validate=false -f ./k8s/hpa.yaml
Para verificar que los pods y el auto-escalado se encuentran operando correctamente:

Bash
kubectl get pods
kubectl get hpa
4. Monitoreo (Prometheus y Grafana)
Despliega los componentes de monitorización ubicados en la carpeta correspondiente para recolectar las métricas del backend:

Bash
kubectl apply -f prometheus/
🛡️ Buenas Prácticas y FinOps (Optimización de Costos)
Seguridad: Se evita la exposición de información sensible mediante el uso de secretos y variables de entorno en el pipeline.

Limpieza de Recursos: Para evitar cargos innecesarios en la nube una vez finalizadas las pruebas o validaciones, se debe destruir la infraestructura ejecutando:

Bash
cd terraform
terraform destroy --auto-approve
