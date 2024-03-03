from akapy.cloudlets import Cloudlet


def test_get_all():
    cloudlet = Cloudlet()
    result = cloudlet.get_all()
    print(result)

    assert result
    assert "cloudletName" in result[0]
