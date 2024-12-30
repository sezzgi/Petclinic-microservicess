FROM eclipse-temurin:17
ENV SPRING_PROFILES_ACTIVE docker
COPY /target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app.jar"]