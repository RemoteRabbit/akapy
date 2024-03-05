# How to use Cloudlets

::: akapy.Cloudlet

## Example Code

```python
import akapy as ak

c = akapy.Cloudlet()

print(c.get_all())
```

### Return

```sh
[
  {
    "serviceVersion": null,
    "apiVersion": "2.0",
    "location": "/cloudlets/api/v2/cloudlet-info/3",
    "cloudletId": 3,
    "cloudletCode": "FR",
    "cloudletName": "FORWARDREWRITE"
  },
  {
    "serviceVersion": null,
    "apiVersion": "2.0",
    "location": "/cloudlets/api/v2/cloudlet-info/0",
    "cloudletId": 0,
    "cloudletCode": "ER",
    "cloudletName": "EDGEREDIRECTOR"
  }
]
```