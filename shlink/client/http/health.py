from shlink.models.status import Status


class Health:
    def get_health(self) -> Status:
        """
        Checks the healthiness of the service, making sure it can access required resources.
        """
        data = self._session.get(self.url + "rest/health").json()
        return Status.from_dict(data)
