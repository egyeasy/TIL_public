# 7강 의존성 주입(Dependency Injection)

- css등 문제가 생기면 mvnw package build 해보는 것도 방법



### 1. 생성자 주입(Spring에서 권장)

```java
@Autowired
public OwnerController(OwnerRepository clinicService) {
    this.owners = clinicService;
}
```

스프링 4.3부터,

클래스에 생성자 하나 뿐이고, 주입받는 애들이 빈으로 등록돼있으면 @Autowired 생략 가능



### 2. Field로 주입

```java
@Autowired
private OwnerRepository owners;
```



css파일이 깨지면 메이븐 빌드 다시 해주면 동작한다.

`BUILD SUCCESS` in colsole : 코드가 제대로 동작함을 의미



### 3. Setter로 주입





- `No qualifying bean` : bean을 아예 정의하지 않았을 때 발생하는 오류



생성자 사용하는 방법 -> ownerRepository를 만드는 것을 강제할 수 있다. (주입해야하는 인자를 넣을 수 없다면 애초에 코드 자체가 성립하지 않는 듯).
순환 참조의 문제 - 서로가 서로를 참조한다면 못 만들게 되고, 앱이 제대로 뜨지 않게 된다. 이땐 생성자 사용 말고 다른 방법을 사용해도 됨.



## 과제

- OwnerController에 PetRepository 주입하기

  #### 필드

  ````java
  @Autowired
  private PetRepository petRepository;
  ````

  #### 생성자

  ````java
  private final PetRepository petRepository;
  
  public OwnerController(OwnerRepository clinicService, PetRepository petReopository) {
      this.owners = clinicService;
      this.petRepository = petRepository;
  }
  ````

  #### setter

  final을 쓰면 안 된다.

  ```java
  private final PetRepository petRepository;
  
  @Autowired
  public void setPetRepository(PetRepository petRepository) {
      this.petRepository = petRepository;
  }
  ```

  