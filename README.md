Instrucciones de Despliegue y Ejecución
1. Prerrequisitos Locales
Asegúrate de tener instaladas las siguientes herramientas en tu entorno de trabajo:

aws-cli configurado con tus credenciales de IAM.

terraform (versión 1.x o superior).

kubectl para la gestión del clúster de Kubernetes.

2. Provisionamiento de Infraestructura (Terraform)
Dirígete a la carpeta de Terraform para levantar la red (VPC) y el clúster de EKS en AWS ejecutando los siguientes comandos en tu terminal:

cd terraform
terraform init
terraform apply --auto-approve

Una vez finalizado, configura tu contexto local para interactuar con el clúster:

aws eks update-kubeconfig --name cluster-bot-trading --region us-east-2

3. Despliegue de Manifiestos en Kubernetes
Desde la raíz del proyecto, aplica los manifiestos de la aplicación y el auto-escalador (HPA):

kubectl apply --validate=false -f ./k8s/backend-deployment.yaml
kubectl apply --validate=false -f ./k8s/hpa.yaml

Para verificar que los pods y el auto-escalado se encuentran operando correctamente:

kubectl get pods
kubectl get hpa

4. Monitoreo (Prometheus y Grafana)
Despliega los componentes de monitorización ubicados en la carpeta correspondiente para recolectar las métricas del backend:

kubectl apply -f prometheus/

Buenas Prácticas y FinOps (Optimización de Costos)
Seguridad: Se evita la exposición de información sensible mediante el uso de secretos y variables de entorno en el pipeline.

Limpieza de Recursos: Para evitar cargos innecesarios en la nube una vez finalizadas las pruebas o validaciones, se debe destruir la infraestructura ejecutando:

cd terraform
terraform destroy --auto-approve
