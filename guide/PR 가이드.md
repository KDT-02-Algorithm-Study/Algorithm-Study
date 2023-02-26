# PR 가이드

## 💡1. Pull

❗**반드시 이 과정 진행 후 작업을 진행해 주세요**❗

* pull을 사용하여 메인 브런치의 최신 내용을 가져온다.

```
git checkout main
git pull origin main
git checkout [브런치이름]
git merge main
```

## 💡2. Commit & Push
* 문제를 풀이 후 `weekN_date/문제`폴더에 자신이 작성한 코드를 넣는다.
  * 간단한 주석을 작성한다.

![](https://user-images.githubusercontent.com/114655005/221214600-1128b5e3-d79d-4965-a7cc-9fa73c59ea71.png)

* 파일 이름 형식은 `문제번호_이름.py` 으로 한다.

  * ex) `1000_홍길동.py`

❗자신의 브런치에 위치하고 있는지 확인❗
```
git branch
```
* 작업 내용을 신중하게 커밋한다. 
```
git status // 변경사항 확인
git add "파일위치/파일명" // 또는 git add .
git commit -m "문제번호_이름"
```
* 신중하게 push한다.
```
git push origin [브런치이름]
```
* 잘못 커밋했을 경우
  * 그냥 덮어씌우거나 [커밋 관리](%EC%BB%A4%EB%B0%8B%20%EA%B4%80%EB%A6%AC.md) 참고

## 💡3. Pull Requests

![](https://user-images.githubusercontent.com/114655005/221224677-3f4f08b4-3749-49fb-b42e-6d33195e18f7.png)

* Compare & pull request 버튼 혹은

![](https://user-images.githubusercontent.com/114655005/221225178-ffb2bc4b-53d7-4d9c-8fa2-909263a8094d.png)

* 오른쪽의 New pull request 버튼을 누른다.

![](https://user-images.githubusercontent.com/114655005/221225572-fef46c23-bbe9-47a0-9d93-c87e46f053f8.png)


* 브런치를 확인한다.
  * `base: main`
  * `compare: 내 브런치`

* PR제목과 간단한 코멘트를 적는다.

* Create pull request 버튼을 누른다.

![화면 캡처 2023-02-27 013022](https://user-images.githubusercontent.com/114655005/221424165-04cab66f-adeb-4dcb-85fc-1d20346de4c5.png)

* 끝

* ~~Merge pull requests 버튼은 코드 리뷰 후에 누르기~~

🍀끝입니다. 다들 파이팅!

> ~~위 가이드는 권장사항으로 조금씩 달라도 됩니다.~~
<br>(잘못커밋해도 되돌릴 방법이 있으니 부담갖지 않으셔도 됩니다.)