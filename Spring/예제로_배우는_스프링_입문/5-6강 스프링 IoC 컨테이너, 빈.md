# 5강 스프링 IoC 컨테이너

컨테이너의 주요 역할 : 빈(bean)을 만들고 엮어주며 제공해준다.

Controller, Repository는 IoC 컨테이너 안에 bean으로 등록되어있다.

Pet은 아니다.

- system/CacheConfiguration 에서 직접 Bean을 등록하는 방법도 있다.(객체를 만들어서 return)
- 컨테이너가 빈들의 의존성을 주입해주게 된다.

- Single Scope : 어떤 어플리케이션 하나를 계속해서 다른 곳에서 사용하는 것. -> IoC 컨테이너를 사용해서 등록된 빈을 손쉽게 이용할 수 있다.

  ```java
  @GetMapping("/bean")
  @ResponseBody
  public String bean() {
      return "bean: " + applicationContext.getBean(OwnerRepository.class) + "\n" + "owners: " + this.owners;  // 둘 다 해시가 같다
  }
  ```

  

# 6강 스프링 빈(Bean)

1. 빈이 아닌것

   ```java
   OwnerController ownerController = new OwnerController();
   ```

2. 빈인 것

   ```java
   OwnerController bean = applicationContext.getBean(OwnerController.class);
   ```

   

### 빈을 어떻게 등록하지?

1. Component Scan

   라이프사이클콜백(인터페이스) - `@Component` annotation을 찾아서 처리해줌. `@ComponentScan`의 명령에 따라 Component scan을 하라고 해준 위치 하위 위치의 모든 곳을 찾아봄.

   @Component 

   @Repository

   @Service

   @Controller

   @Configuration

   - Repository는 JPA에 의해 자동으로 Bean으로 등록이 됨.

2. Bean으로 직접 등록

   ```java
   @Configuration
   public class SampleConfig {
       @Bean
       public SampleController sampleController() {
           return new SampleController(); // 객체를 return하면 이것이 bean이 됨
       }
   }
   ```

   @configuration 노테이션 안에 @Bean을 정의하여 씀

   그렇게 만든 빈은 `@Controller` 등으로 명시해줄 필요도 없어진다.

   @configuration도 컴포넌트이기 때문에 스캔이 됨.



### 빈을 꺼내서 쓰는 법

1. 생성자를 통해 주입받는 법

2. @Autowired annotation

   ```java
   @Autowired
   private OwnerRepository owners;
   ```

   