"""
    Python library for Symantec Trust Center Enterprise API

        https://developers.websecurity.symantec.com/api

    @author     Benton Snyder
    @website    http://bensnyde.me
    @email      benton@bensnyde.me
    @created    1/5/16
    @updated    1/5/16
"""

import requests
import urllib

API_ENDPOINT = 'https://pilot-trustcenter-enterprise.websecurity.symantec.com/service/api/'     # Development
#API_ENDPOINT = 'https://trustcenter-enterprise.websecurity.symantec.com/service/api/'          # Production

class Symantec:
    def __query(self, resource, data):
        url = "%s%s" % (API_ENDPOINT, resource)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = urllib.urlencode(data)

        r = requests.post(url, headers=headers, data=data)
        if r.status_code == 200:
            return r.text
        else:
            r.raise_for_status()

    def enroll_certificate(self, kwargs):
        """
            Enroll for a new certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            certProductType:        req str Certificate type ["SecureSite", "SecureSitePro", "SecureSiteEV", "SecureSiteProEV"]
            csr:                    req str Certificate Signing Request
            serverType:             req str Server type ["Microsoft", "Apache", "Other"]
            validityPeriod:         req int Number of years certificate is valid for [1,2,3]
            signatureAlgorithm:     req str Certificate encryption and signature hash algorithm ["sha1WithRSAEncryption", "sha256WithRSAEncryptionMixedChain", "sha256WithRSAEncryptionFullChain", "DSAwithSHA256", "ECDSAwithSHA256"]
            email:                  opt str Comma-seperated list of email addresses to send certificate to
            extraLicenses:          opt str Number of additional server licenses needed
            subjectAltNames:        opt str Comma-seperated list of Subject Alternative Names
            ctLogOptOut:            opt str Disable Certificate Transparency ['no', 'yes']
            malwareScanStartPoint:  opt str Start page for malware scanning
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificateEnroll", kwargs)


    def renew_certificate(self, kwargs):
        """
            Renew an expiring or expired certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            orderNumber:            req str Order number or actual certificate string to be renewed
            certProductType:        req str Certificate type ["SecureSite", "SecureSitePro", "SecureSiteEV", "SecureSiteProEV"]
            csr:                    req str Certificate Signing Request
            serverType:             req str Server type ["Microsoft", "Apache", "Other"]
            validityPeriod:         req int Number of years certificate is valid for [1,2,3]
            signatureAlgorithm:     req str Certificate encryption and signature hash algorithm ["sha1WithRSAEncryption", "sha256WithRSAEncryptionMixedChain", "sha256WithRSAEncryptionFullChain", "DSAwithSHA256", "ECDSAwithSHA256"]
            email:                  opt str Comma-seperated list of email addresses to send certificate to
            extraLicenses:          opt str Number of additional server licenses needed
            subjectAltNames:        opt str Comma-seperated list of Subject Alternative Names
            usePredecessorSans:     opt str Indicates whether to use SANs from the previous certificate ['True', 'False']
            ctLogOptOut:            opt str Disable Certificate Transparency ['no', 'yes']
            malwareScanStartPoint:  opt str Start page for malware scanning
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificateRenew", kwargs)

    def replace_certificate(self):
        """
            Replace an existing, valid or revoked certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            orderNumber:            req str Order number or actual certificate string to be renewed
            certProductType:        req str Certificate type ["SecureSite", "SecureSitePro", "SecureSiteEV", "SecureSiteProEV"]
            csr:                    req str Certificate Signing Request
            serverType:             req str Server type ["Microsoft", "Apache", "Other"]
            validityPeriod:         req int Number of years certificate is valid for [1,2,3]
            signatureAlgorithm:     req str Certificate encryption and signature hash algorithm ["sha1WithRSAEncryption", "sha256WithRSAEncryptionMixedChain", "sha256WithRSAEncryptionFullChain", "DSAwithSHA256", "ECDSAwithSHA256"]
            email:                  opt str Comma-seperated list of email addresses to send certificate to
            extraLicenses:          opt str Number of additional server licenses needed
            subjectAltNames:        opt str Comma-seperated list of Subject Alternative Names
            usePredecessorSans:     opt str Indicates whether to use SANs from the previous certificate ['True', 'False']
            ctLogOptOut:            opt str Disable Certificate Transparency ['no', 'yes']
            malwareScanStartPoint:  opt str Start page for malware scanning
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificateReplace", data)

    def revoke_certificate(self):
        """
            Replace an existing, valid or revoked certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            orderNumber:            req str Order number or actual certificate string to be renewed
            reason:                 req int Reason for revoking the certificate [1 (key compromise), 2 (affiliation changed) ,3 (superseded) ,4 (cessation of operation)]
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificateRevoke", kwargs)


    def pickup_certificate(self):
        """
            Replace an existing, valid or revoked certificate

        Parameters
            brand:                  req str Brand name ['symantec']
            userName:               req str Symantec Trust Center Enterprise account username
            password:               req str Symantec Trust Center Enterprise account password
            orderNumber:            req str Order number or actual certificate string to be renewed
            format:                 req str Certificate format ['pkcs7', 'x509']
        Returns
            Success:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    orderNumber
            Failure:
                CertificateServiceResponse
                    statusCode
                    statusMessage
                    errorList
                        error
                            errorMessage
                            fieldName
        """
        return self.__query("certificatePickup", data)


# Usage example
print Symantec().enroll_certificate({
    'brand': 'symantec',
    'userName': 'exampleuser',
    'password': 'examplepassword',
    'certProductType': 'SecureSite',
    'serverType': 'Apache',
    'validityPeriod': 1,
    'signatureAlgorithm': 'sha256WithRSAEncryptionMixedChain',      #
    'csr':
"""%0AMIICqDCCAZACAQAwYzELMAkGA1UEBhMCVVMxEzARBgN
VBAgTCkNhbGlmb3JuaWEx%0AFjAUBgNVBAcTDU1vdW50YW
luIFZpZXcxFDASBgNVBAoTC3N0Y2UyMDEzMUVWMREw%0AD
wYDVQQDEwhvMmlzcC5jejCCASIwDQYJKoZIhvcNAQEBBQA
DggEPADCCAQoCggEB%0AALRCyLR1E%2FQ6uolRnh4xNDLG
nu1NS5%2B8MIKq%2BwX%2FsjM4EsOlnvYARA9T%2BT5Zmf
aA%0AVRxpIfRzy5BimCv7x9tLWbaoZTRlX9sNVIP7vMqcN
%2Bga1kQ%2ByicSIDSOew2r%2BL1d%0AiJRVgeUvexOWMQ
TuYldBEh80CtfRrCoOP%2BO2NWbKqkKHjDK2PNdhwtbyy%
2Fa3tOvh%0A%2F0LDW%2FDO3k3jwIR28stwgaJdrwNramp
%2BMk%2BOnJM%2Fvw31OoUvrrw%2BzAoHvjQ%2BQ7ex%0A
jzsBTmWisIQ7uFfQ%2BPDCTqesU3e8EYb%2FAZzf1aSVLL
XrjIgBi6d25Zl3el5%2BTsO8%0ALTaI2xx1pK8qSJSEqi4
EgxcCAwEAAaAAMA0GCSqGSIb3DQEBCwUAA4IBAQAJ%2FiM
B%0A5AW4hzLxhI2G0akjSbmwtPjAfnSqNL4WfIKv2Jc4ed
X7wv%2Bf9SLnk84Oj%2BpT9N7R%0AsK8qnhHEbHU00fN64
dIG%2BhUyEoO3u%2BO%2FZzDA0DWzuBVcG%2Buythe7%2B
dd7Mhxm%2Fgj2%0AKajKaaoA0jqXYntnrYphm3x99JhMRd
AhU4%2Bh%2FJQ9cUOYDWrXk%2By%2FIvVLegKQS0vr%0AZ
jzm6ujI5aPgRsIinXrrPU9jUIYMYrzrkgA%2ByXn31aL3V
XJ5seSIJd5oMo9dwE6T%0APteWG0zupgYUfvluBe6H%2FG
tla81wKiylC0KUM9CeuT9TQlZnkvfvbbTtHTHC6GDD%0AZ
hA1ofxQTmsGpqyY%0A"""
})
