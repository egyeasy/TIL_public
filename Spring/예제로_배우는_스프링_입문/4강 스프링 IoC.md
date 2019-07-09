# 4강 스프링 IoC

## Inversion of Control

'제어권이 역전되었다'는 의미

martin fowler의 글을 보면 이해할 수 있을 것



- 일반적인 (의존성에 대한 제어권) : 내가 사용할 의존성은 내가 만든다.

  ```java
  class OwnerController {
      private OwnerRepository repository = new OwnerRepository();
  }
  ```

  

- IoC : 내가 사용할 의존성을 누군가 알아서 주겠지

  ```java
  class OwnerController {
      private OwnerRepository repo;
      
      public OwnerController(OwnerRepository repo) {
          this.repo = repo;
      }
      
      // repo를 사용
  }
  ```

  ```java
  class OwnerControllerTest {
      @Test
      public void create() {
          OwnerRepository repo = new OwnerRepository();
          OwnerController controller = new OwnerController(repo);
      }
  }
  ```

  



### OwnerController.java

소스에서,

`OwnerRepository`가 없으면 `OwnerController`를 못 만들도록 되어있다.

-> `this.owners`는 항상 null이 아니게 된다.



### OwnerControllerTests.java

```java
@MockBean
private OwnerRepository owners;
```

테스트에서 레포지토리 타입의 owners 객체를 만든다. 이걸 Bean(spring에서 관리하는 객체)이라고 한다.

스프링은 Bean의 의존성을 관리(특정한 annotation을 따라 필요한 의존성을 주입)해서 객체 안의 값을 채워줌.



