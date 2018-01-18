# ![Malshare](https://s13.postimg.org/mex3nuox3/debug.png) Malshare Data

## Usage

### Latest

```python
import malshare
print(malshare.Malshare.get_latest()[:2])
```

```javascript
[
    Malshare(hash='af0ea177101c8427e299afd20435b77ae0f2197faf49b6e66d842959c7c2e018', date=datetime.datetime(2018, 1, 17, 0, 0)),
    Malshare(hash='663b223915349f830b8b8a92096916728e7dd9aace088f343bf0320d2506dd1b', date=datetime.datetime(2018, 1, 17, 0, 0))
]
```

### Get All Dates

```python
import malshare
print(malshare.Malshare.get_all_dates()[:2])
```

```javascript
[
    Malshare(hash='ecd18f93c61c7f1a9c91fd52638a581d0d052bb085aaa51e08b858ef9a421507', date=datetime.datetime(2017, 9, 14, 0, 0)),
    Malshare(hash='241043ea2dc757dad69a84dc9b6e545cf93ef29b272a1bf098690d95b37e8f42', date=datetime.datetime(2017, 9, 14, 0, 0))
]
```